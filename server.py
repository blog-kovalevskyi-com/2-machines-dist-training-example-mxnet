import os
os.environ.update({
  "DMLC_ROLE": "server",
  "DMLC_PS_ROOT_URI": "172.31.89.150",
  "DMLC_PS_ROOT_PORT": "9000",
  "DMLC_NUM_SERVER": "1",
  "DMLC_NUM_WORKER": "2",
  "PS_VERBOSE": "0"
})
import mxnet
kv_store = mxnet.kv.create('dist_sync')
