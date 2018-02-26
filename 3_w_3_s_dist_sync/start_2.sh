source activate mxnet_p36
python server.py &
python image-classification/train_imagenet.py \
--gpu 0,1,2,3,4,5,6,7 --batch-size 960 --num-epochs 10 \
--data-nthreads 40 --disp-batches 20 \
--network resnet-v1 --num-layers 50 \
--max-random-shear-ratio 0 \
--min-random-scale 0.533 \
--max-random-rotate-angle 0 \
--max-random-h 0 --max-random-l 0 \
--max-random-s 0 --max-random-aspect-ratio 0 \
--kv-store dyst_sync \
--benchmark 1 &
