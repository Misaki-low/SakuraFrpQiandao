import logging
import sys

from config import Config
from automation import CheckInAutomation

logger = logging.getLogger(__name__)


def main() -> int:
    """主函数：返回退出码，0 成功，非 0 失败（让 Actions 能正确显示红叉并触发重试）"""
    try:
        # 加载配置
        config = Config.from_env()
        logger.info(f"使用账户: {config.sakurafrp_user}")

        # 执行自动签到
        automation = CheckInAutomation(config)
        if automation.run():
            logger.info("签到成功")
            return 0

        logger.error("签到未完成")
        return 1

    except ValueError as e:
        logger.error(f"配置错误: {e}")
        return 2
    except Exception as e:
        logger.error(f"程序执行失败: {e}", exc_info=True)
        return 3


if __name__ == "__main__":
    sys.exit(main())
