#include "dawn/native/DawnNative.h"
#include <cstdio>
#include <memory>
#include <iostream>
int main(int argc, const char* argv[]) {
    printf("hello, here i am.\n");

    //dawnProcSetProcs(&dawn::native::GetProcs());

    // auto toggles = dawn::native::AllToggleInfos();
    // std::cout << "Toggles: " << toggles.size() << "\n";
    // std::cout << "=======\n";
    // bool first = true;
    // for (const auto* info : toggles) {
    //     if (!first) {
    //         std::cout << "\n";
    //     }
    //     first = false;
    //     std::cout << "  Name: " << info->name << "\n";
    //     std::cout << info->description << "\n";
    //     std::cout << "    " << info->url << "\n";
    // }
    // std::cout << "\n";

    auto instance = std::make_shared<dawn::native::Instance>();
    printf("Got instance %p, looking for adapters...\n", instance.get());

    wgpu::RequestAdapterOptions options {
        nullptr,
        nullptr,
        wgpu::PowerPreference::HighPerformance,
        wgpu::BackendType::Undefined,
        false,
        false
    };
    auto adapters = instance->EnumerateAdapters(&options);

    printf("Got %zu adapters\n", adapters.size());

    for (auto& adapter: adapters) {
        WGPUAdapterInfo info {};
        auto status = adapter.GetInfo(&info);
        printf("status %d\n", status);
        printf("Got info %s\n", info.architecture);
    }
    
}