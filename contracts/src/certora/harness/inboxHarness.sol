// Copyright 2021-2022, Offchain Labs, Inc.
// For license information, see https://github.com/nitro/blob/master/LICENSE
// SPDX-License-Identifier: BUSL-1.1

pragma solidity ^0.8.4;

import "../munged/inboxOldMunged.sol";

contract inboxHarness is Inbox{
    function getBridge()external returns(IBridge){
        return bridge;
    }
    function getInitialized() external returns(bool){
        return _initialized;
    }
    function getInitializing() external returns(bool){
        return _initializing;
    }

    function getProxyOwner() external returns(address admin){
          bytes32 slot = 0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103;
          assembly {
            admin := sload(slot)
        }
    }
        
    }
