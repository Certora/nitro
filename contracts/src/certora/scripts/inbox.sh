if [[ "$1" ]]
then
    RULE="--rule $1"
fi

certoraRun contracts/src/certora/harness/inboxHarness.sol \
    --verify inboxHarness:contracts/src/certora/specs/inbox.spec \
    $RULE \
    --solc solc8.15 \
    --send_only \
    --staging \
    --rule_sanity \
    --optimistic_loop \
    --loop_iter 3
    # --debug \
    # --packages_path $(pwd)/contracts/node_modules/@openzeppelin
# certoraRun contracts/certora/harness/inbox.sol \
    # --msg "ProtocolFeeSplitterHarness:setup.spec $1 "
    # --link ProtocolFeeSplitterHarness:protocolFeesCollectorMemory=ProtocolFeesCollector \
    # certora/helpers/DummyERC20Impl.sol \
    # --debug
    # --debug
    # --settings -useBitVectorTheory \
    # certora/munged/vault/contracts/ProtocolFeesCollector.sol \
    # certora/harness/VaultHelpersHarness.sol:VaultHelpers \
