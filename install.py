# 安装依赖项


import launch


# for dep in ['jieba','nanoid','oss2','xlrd','mq_http_sdk','tenacity','colorama','opencv-contrib-python',
#             'dlib','face_recognition','pillow-avif-plugin','segment-anything']:
#     if not launch.is_installed(dep):
#         launch.run_pip(f'install {dep}',f'{dep} for lubanai extension')

# for dep in ['onnxruntime','pymatting','pooch']:
#     if not launch.is_installed(dep):
#         launch.run_pip(f'install{dep}',f'{dep} for onnxruntime')

# if not launch.is_installed("mobile_sam"):
#     launch.run_pip('install git+https://github.com/ChaoningZhang/MobileSAM.git','mobile_sam')


# for dep in ['jieba','nanoid','xlrd','tenacity','colorama','opencv-contrib-python',
#             'dlib',]:
#     if not launch.is_installed(dep):
#         # 启用镜像下载
#         launch.run_pip(f'install -i https://pypi.tuna.tsinghua.edu.cn/simple {dep}',f'{dep} for lubanai extension')

# if not launch.is_installed("rembg"):
#     launch.run_pip('install -i https://pypi.tuna.tsinghua.edu.cn/simple rembg==2.0.38 --no-deps','rembg')