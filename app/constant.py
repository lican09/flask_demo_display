# -*- coding=utf-8 -*-


class _const:

    pass


const = _const()

const.SUCCESS = 10000
const.AUTH_ERROR = 10001
const.ADD_ERROR = 10002
const.ORDER_NUM_ADD_ERROR = 10003
const.OVER_MAX_SEARCH_TIMES = 10004


const.MSG = {
    const.SUCCESS: 'success',
    const.AUTH_ERROR: 'auth error',
    const.ADD_ERROR: 'add error',
    const.ORDER_NUM_ADD_ERROR: 'order number add error',
    const.OVER_MAX_SEARCH_TIMES: 'over max avaliable search times!',
}

# celery任务队列
const.INPUT_QUEUE = 'input_q'
const.RETRY_INPUT_QUEUE = 'retry_input_q'
const.IMAGE_MONITOR_QUEUE = 'image_monitor_q'
