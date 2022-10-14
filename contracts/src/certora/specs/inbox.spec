// import "../helpers/erc20.spec"
// import "../../src/bridge/Ibridge.sol"


methods{
    setRevenueSharingFeePercentage(bytes32,uint256)
    getInitialized() envfree
    getInitializing() envfree
    getBridge() envfree
    getProxyOwner() envfree
}

// rule to check if an address other than owner can change the bridge
// FAILS as initialize function changes the bridge and can be called by anyone
// This would be a problem if the initialize function can be called twice
rule onlyProxyOwnerCanChangeBridge(env e, method f){
    address owner;
    // owner = getProxyOwner();
    address bridgeBefore;
    bridgeBefore = getBridge();
    calldataarg args;
    
    f(e, args);

    address bridgeAfter;
    bridgeAfter = getBridge();
    assert bridgeAfter != bridgeBefore => e.msg.sender == getProxyOwner(),"only owner can change the bridge";
}

// rule to check if we can call the initialize function twice with different parameters
// this rule passes. The initialized flag is true after the first call so the 
// second call reverts. If the flag could be turned false, it could be an issue.

rule callingInitializeTwice(){
    env e1;
    calldataarg args1;
    env e2;
    calldataarg args2;
    initialize(e1, args1);
    initialize@withrevert(e1, args1);
    assert lastReverted;
}

// rule to verify that once the contract has been initialized, it cannot be uninitialized
// FAILS: postUpgradeInit function sets the initialzed flag to false
rule cannotUninitializeContract(method f){
    
    // Initialization state before
    bool initializedBefore = getInitialized();
    bool initializingBefore = getInitializing();
    
    env e;
    calldataarg args;
    f(e, args);

    bool initializedAfter = getInitialized();
    bool initializingAfter = getInitializing();

    assert initializedBefore => initializedAfter, "Once initialized, the initialized flag cannot be changed";
}

// rule showing the complete attack
rule cannotInitializeTwice(method f){
    env e1;
    env e2;
    env e3;
    calldataarg args1;
    calldataarg args2;
    calldataarg args3;

    bool initializedBefore = getInitialized();
    bool initializingBefore = getInitializing();
    address bridge;

    initialize(e1, args1);

    bool initialized1 = getInitialized();
    bool initializing1 = getInitializing();

    f(e2, args2);

    bool initializedAfter = getInitialized();
    bool initializingAfter = getInitializing();
    
    initialize@withrevert(e3, args3);
    
    assert lastReverted,"initialize can only be called once";

}

