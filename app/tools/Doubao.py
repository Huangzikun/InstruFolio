from flask import current_app
from volcenginesdkarkruntime import Ark

class Doubao:
    # 单例控制变量
    _instance = None
    _initialized = False  # 防止重复初始化

    def __new__(cls):
        """确保仅创建一个实例"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """初始化 Ark 客户端（仅执行一次）"""
        if not self._initialized:  # 仅在首次实例化时执行初始化
            self.client = Ark(
                base_url="https://ark.cn-beijing.volces.com/api/v3",
                api_key=current_app.config['ARK_API_KEY'],
            )
            self._initialized = True  # 标记为已初始化

    def query(self, system_prompt, user_query):
        completion = self.client.chat.completions.create(
            # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
            model="doubao-seed-1-6-250615",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query},
            ],
        )
        return completion.choices[0].message.content
