#include "gpu/gpu.h"
#include <cstdio>

int main()
{
    auto context = gpu::createContext();
    // auto instance = wgpuCreateInstance(nullptr);
    // printf("Do I have an instance? %p\n", instance);
    // WGPURequestAdapterCallback callback = [](WGPURequestAdapterStatus status, WGPUAdapter adapter, char const * message, void * userdata)
    // {
    //     printf("Adapter callback: %x\n", status);
    //     if (adapter) {
    //         WGPUAdapterInfo info {

    //         };
    //         auto ret = wgpuAdapterGetInfo(adapter, &info);
    //         printf("result=%d\n", ret);
    //         printf("adapter architecture=%s\n", info.architecture);
    //     }
    // };
    // wgpuInstanceRequestAdapter(instance, nullptr, callback, nullptr);
    printf("done...?\n");
}