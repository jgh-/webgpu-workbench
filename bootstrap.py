import os
import subprocess
import sys
import shutil
import urllib.request

def prep_dawn(prep_dir, src_dir):
    if not os.path.isdir(f"{prep_dir}/dawn"):
        print("Cloning Dawn")
        subprocess.call(["git", "clone", "--depth=1", "https://dawn.googlesource.com/dawn", f"{prep_dir}/dawn"])
        os.makedirs(f"{prep_dir}/dawn/build", exist_ok=True)
    
    os.chdir(f"{prep_dir}/dawn")
    print("Downloading Dawn dependencies")
    subprocess.call([sys.executable, f"{prep_dir}/dawn/tools/fetch_dawn_dependencies.py", "--use-test-deps"])
    os.chdir(f"{prep_dir}/dawn/build")
    print("Configuring Dawn")
    env = os.environ.copy()
    if env.get("CXXFLAGS"):
        env["CXXFLAGS"] = f"{env.get('CXXFLAGS')} /DDAWN_ENABLE_ASSERTS=1"
    else:
        env["CXXFLAGS"] = "/DDAWN_ENABLE_ASSERTS=1"
    subprocess.call(["cmake",
                    "-DDAWN_ENABLE_INSTALL=ON",
                    "-DDAWN_BUILD_MONOLITHIC_LIBRARY=ON",
                    "-DCMAKE_BUILD_TYPE=Debug",
                    "-DBUILD_SAMPLES=ON",
                    "-DDAWN_ENABLE_PIC=ON",
                    "-DBUILD_SHARED_LIBS=OFF",
                    f"-B{prep_dir}/dawn/build",
                    f"{prep_dir}/dawn"
                    ], env=env)
    print("Building Dawn")
    subprocess.call(["cmake", "--build", f"{prep_dir}/dawn/build", "--config", "Debug", "-j"])
    print(f"Installing Dawn in '{src_dir}/third_party'")
    subprocess.call(["cmake", "--install", f"{prep_dir}/dawn/build", "--config", "Debug", "--prefix", f"{src_dir}/third_party"])

def prep_gpucpp(prep_dir, src_dir):
    print("Download GPU.CPP")
    os.makedirs(f"{src_dir}/third_party/include/gpu/utils", exist_ok=True)
    urllib.request.urlretrieve("https://raw.githubusercontent.com/AnswerDotAI/gpu.cpp/main/gpu.h", f"{src_dir}/third_party/include/gpu/gpu.h")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/AnswerDotAI/gpu.cpp/main/utils/logging.h", f"{src_dir}/third_party/include/gpu/utils/logging.h")

if __name__ == "__main__":
    src_dir = os.path.abspath(os.path.dirname(__file__))
    prep_dir = f"{src_dir}/.prep"
    os.makedirs(f"{src_dir}/third_party", exist_ok=True)
    os.makedirs(f"{src_dir}/.prep", exist_ok=True)
    prep_dawn(prep_dir, src_dir)
    prep_gpucpp(prep_dir, src_dir)
    print("Cleaning up..")
    #shutil.rmtree(prep_dir)
