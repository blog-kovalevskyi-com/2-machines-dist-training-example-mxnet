import os
os.environ.update({
  "DMLC_ROLE": "scheduler",
  "DMLC_PS_ROOT_URI": "0.0.0.0",
  "DMLC_PS_ROOT_PORT": "9000",
  "DMLC_NUM_SERVER": "1",
  "DMLC_NUM_WORKER": "2",
  "PS_VERBOSE": "2"
})
worker_env = os.environ.copy()
import mxnet
kv_store = mxnet.kv.create('dist_async')
