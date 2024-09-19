def preload(parser):

    parser.add_argument(
        "--rocketmq",
        action="store_true",
        help="启动rocketmq",
        default=None
    )
    parser.add_argument(
        "--env",
        type=str,
        help="运行环境: daily, staging, production",
        default='daily'
    )
    parser.add_argument(
        "--appname",
        type=str,
        help="隔离环境: ICBU, LubanAI_TB, Comic, ProductBatch",
        default='LubanAI_TB'
    )
    parser.add_argument(
        "--download-model",
        action="store_true",
        help="下载模型",
        default=False
    )
    parser.add_argument(
        "--model-checksum",
        action="store_true",
        help="校验模型 checksum",
        default=False
    )