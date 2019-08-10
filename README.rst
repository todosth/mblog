开发流程
===============
变更依赖库时

------------------
1.更新 setup.py 的 install_requires
2.按以下流程更新环境
    - virtualenv --clear .venv
    - pip install -e ./mblog
    - pip freeze > requirements.txt
3.将requiremevnts.txt提交至版本库