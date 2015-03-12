from pkg_resources import declare_namespace
declare_namespace(__name__)

import crawler
import crawlnmine
import miner
__all__ = ['crawler', 'crawlnmine', 'miner']