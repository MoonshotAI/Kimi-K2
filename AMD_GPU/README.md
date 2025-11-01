## AMD GPU Installation and Testing Guide
### Please follow the steps here to install and run GLM models on AMD MI300X GPU.
### Step By Step Guide
#### Step 1
Launch the Rocm-vllm docker:

```shell
docker run -it --rm \
  --cap-add=SYS_PTRACE \
  -e SHELL=/bin/bash \
  --network=host \
  --security-opt seccomp=unconfined \
  --device=/dev/kfd \
  --device=/dev/dri \
  -v /:/workspace \
  --group-add video \
  --ipc=host \
  --name vllm_GLM \
rocm/vllm-dev:nightly
```

#### Step 2
  Huggingface login

```shell
   huggingface-cli login 
```   

#### Step 3
Run the vllm online serving
Sample Command

```shell
VLLM_USE_V1=1 vllm serve moonshotai/Kimi-K2-Instruct -tp 8 --gpu-memory-utilization 0.95 --no-enable-prefix-caching --trust-remote-code 
```
