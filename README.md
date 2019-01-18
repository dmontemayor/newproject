# newproject
Template for new conda based projects.

## Getting Started
+ Follow directions to download miniconda installer for
[Windows](https://conda.io/docs/user-guide/install/windows.html),
[MacOS](https://conda.io/docs/user-guide/install/macos.html),
or [Linux](https://conda.io/docs/user-guide/install/linux.html).
Run the installer script, e.g. for MacOS open a terminal and run:
```
bash Miniconda3-latest-MacOSX-x86_64.sh
```
which will open an installer screen that will walk you through installation.
+ Double check conda is updated.
```
conda update -n base conda
```
+ Create a virtual environment named 'newproject'
```
conda create --file requirements.txt -c conda-forge -n newproject
```
When prompted new packages will be installed, procceed by pressing `y`.
+ Activate `newproject` virtual environment
```
conda activate newproject
```
### Manually install some packages
 Depending on the way packages keep up with conda, you may need to manually add some packages after you activate the environment.
 ```
conda install -c conda-forge <somepackage>
conda update -y --all
```
If you are using this project template then you also probably want to install the CRMP package developed by our lab. First clone the [CRPM repository](https://github.com/dmontemayor/CRPM) from github. This is private repo while under development contact [Daniel Montemayor](mailto:montemayord2@uthscsa.edu) for permissions. Navigate to the downloaded CRPM project and install the package into your now active `newproject` environment.
```
cd /path/to/CRPM/project
python setup.py install
```
You should see something like
```
Installed /Users/.../miniconda3/envs/newproject/lib/python3.7/site-packages/crpm-0.1-py3.7.egg
```
indicating the crpm egg was laid in the miniconda 'newproject' environment. Now you can navigate back to the 'newproject' folder.
### Upating, Deactivating, and Removing the `newproject` environment.
+ Update virtual environment (when necessary)
```
conda env update -n newproject -f requirements.txt
```
+ Integration testing (for devs)- Check for code style and run tests
```
./integration.sh
```
+ To deactivate environment, use
```
conda deactivate
```
+ To remove an environment, use
```
conda env remove -n newproject
```

## Running newproject analysis

Before you begin make sure you have the `newproject` environment activated. Refer to
the `Gettting Started` section for instructions on how to do this.
End-to-End analysis is conducted by running the [workflow script](workflow/newproject.py).
```
python workflow/newproject.py
```
This will reproduce all results, figures, and tables and store them in the `results` folder.
[A detailed description of the workflow](suppl/WorkflowDetails.md) is provided in the `suppl` folder.
## Project Plan
The project's [plan of action](goals/Plan.md) is located in the 'goals' folder.
