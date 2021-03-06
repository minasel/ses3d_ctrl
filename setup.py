from setuptools import setup

setup(
    name="ses3d_ctrl",
    version="0.1",
    py_modules=["ses3d_ctrl"],
    install_requires=[
        "Click",
        "six",
        "arrow",
        "psutil",
        "enum34",
        "numpy",
        "h5py",
        "xarray"
    ],
    entry_points="""
        [console_scripts]
        agere=ses3d_ctrl.ses3d_ctrl:cli
    """
)
