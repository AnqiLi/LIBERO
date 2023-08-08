# read the contents of your README file
from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "./README.md"), encoding="utf-8") as f:
    lines = f.readlines()

# remove images from README
lines = [x for x in lines if ".png" not in x]
long_description = "".join(lines)

setup(
    name="libero",
    packages=[package for package in find_packages() if package.startswith("libero")],
    install_requires=[],
    eager_resources=["*"],
    include_package_data=True,
    python_requires=">=3",
    description="LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
    author="Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone",
    # url="https://github.com/ARISE-Initiative/robosuite",
    author_email="bliu@cs.utexas.edu, yifengz@cs.utexas.edu",
    version="0.1.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "hydra-core==1.2.0",
        "numpy==1.21.6",
        "wandb==0.13.1",
        "easydict==1.9",
        "transformers==4.21.1",
        "opencv-python==4.6.0.66",
        "robomimic==0.2.0",
        "einops==0.4.1",
        "thop==0.1.1-2209072238",
        "robosuite",
        "bddl==1.0.1",
        "future==0.18.2",
        "matplotlib==3.5.3",
        "cloudpickle==2.1.0",
        "gym==0.25.2",
        "torch==1.11.0",
        "torchvision==0.12.0",
        "torchaudio==0.11.0",
    ],
    entry_points={
        "console_scripts": [
            "lifelong.main=libero.lifelong.main:main",
            "lifelong.eval=libero.lifelong.evaluate:main",
            "libero.config_copy=scripts.config_copy:main",
            "libero.create_template=scripts.create_template:main",
        ]
    },
)
