# cat common/dbutils/bucket.go| grep '=' | grep byte | sed 's/\[\]byte(//' | sed 's/)//' | awk '{print $1 $2 $3".encode()"}' | grep -v '//'
import common

PlainStateBucket = "PLAIN-CST2".encode()
PlainContractCodeBucket = "PLAIN-contractCode".encode()
PlainAccountChangeSetBucket = "PLAIN-ACS".encode()
PlainStorageChangeSetBucket = "PLAIN-SCS".encode()
CurrentStateBucket = "CST2".encode()
AccountsHistoryBucket = "hAT".encode()
StorageHistoryBucket = "hST".encode()
CodeBucket = "CODE".encode()
ContractCodeBucket = "contractCode".encode()
IncarnationMapBucket = "incarnationMap".encode()
AccountChangeSetBucket = "ACS".encode()
StorageChangeSetBucket = "SCS".encode()
IntermediateTrieHashBucket = "iTh".encode()
DatabaseInfoBucket = "DBINFO".encode()
DatabaseVerisionKey = "DatabaseVersion".encode()
HeadHeaderKey = "LastHeader".encode()
HeadBlockKey = "LastBlock".encode()
HeadFastBlockKey = "LastFast".encode()
FastTrieProgressKey = "TrieSync".encode()
HeaderPrefix = "h".encode()
HeaderTDSuffix = "t".encode()
HeaderHashSuffix = "n".encode()
HeaderNumberPrefix = "H".encode()
BlockBodyPrefix = "b".encode()
BlockReceiptsPrefix = "r".encode()
TxLookupPrefix = "l".encode()
BloomBitsPrefix = "B".encode()
PreimagePrefix = "secure-key-".encode()
ConfigPrefix = "ethereum-config-".encode()
BloomBitsIndexPrefix = "iB".encode()
BloomBitsIndexPrefixShead = "iBshead".encode()
LastPrunedBlockKey = "LastPrunedBlock".encode()
LastAppliedMigration = "lastAppliedMigration".encode()
StorageModeHistory = "smHistory".encode()
StorageModeReceipts = "smReceipts".encode()
StorageModeTxIndex = "smTxIndex".encode()
StorageModePreImages = "smPreImages".encode()
StorageModeIntermediateTrieHash = "smIntermediateTrieHash".encode()
SyncStageProgress = "SSP2".encode()
SyncStageUnwind = "SSU2".encode()
CliqueBucket = "clique-".encode()
Senders = "txSenders".encode()

# cat common/dbutils/bucket.go| grep '=' | grep byte | sed 's/\[\]byte(//' | sed 's/)//' | awk '{print $3}' | grep -v '//' | grep -v '='  | tr '\n' ','
buckets = ["PLAIN-CST2", "PLAIN-contractCode", "PLAIN-ACS", "PLAIN-SCS", "CST2", "hAT", "hST", "CODE", "contractCode",
           "incarnationMap", "ACS", "SCS", "iTh", "DBINFO", "DatabaseVersion", "LastHeader", "LastBlock",
           "LastFast", "TrieSync", "h", "t", "n", "H", "b", "r", "l", "B", "secure-key-", "ethereum-config-", "iB",
           "iBshead", "LastPrunedBlock", "lastAppliedMigration", "smHistory",
           "SSP2", "SSU2", "clique-", "txSenders",]


def isHeaderHashKey(k):
    l = common.BlockNumberLength + 1
    return len(k) == l and k[l - 1:] == HeaderHashSuffix


def isHeaderTDKey(k):
    l = common.BlockNumberLength + common.HashLength + 1
    return len(k) == l and bytes.Equal(k[l - 1:], HeaderTDSuffix)


def isHeaderKey(k):
    l = common.BlockNumberLength + common.HashLength
    if len(k) != l:
        return False
    return (not isHeaderHashKey(k)) and (not isHeaderTDKey(k))
