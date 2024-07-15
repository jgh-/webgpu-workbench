#include "gpu/gpu.h"
#include <cstdio>

int main()
{
    auto context = gpu::createContext();
    WGPUAdapterInfo info {};
    wgpuAdapterGetInfo(context.adapter, &info);
    printf("Using adapter=%s\n", info.description);

    printf("done...?\n");
}