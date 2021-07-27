from Params.params import get_parameter


class OrderList:
    """根据条件筛选订单信息"""
    params = get_parameter('order_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class OrderExport:
    """导出订单信息"""
    params = get_parameter('order_export')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PayList:
    """根据条件获取订单流水列表"""
    params = get_parameter('pay_list')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetPay:
    """根据orderPayId获取相应的支付单信息"""
    params = get_parameter('pay_get')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PaySaveNote:
    """保存审核备注的修改"""
    params = get_parameter('pay_saveNote')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PayRefused:
    """支付单审核-打回"""
    params = get_parameter('pay_refused')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PayRefusedBatch:
    """支付单审核-批量打回"""
    params = get_parameter('pay_refusedBatch')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class Paycheck:
    """支付单审核-复核通过"""
    params = get_parameter('pay_check')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PaycheckBatch:
    """支付单审核-复核通过"""
    params = get_parameter('pay_checkBatch')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PayExport:
    """导出支付单信息"""
    params = get_parameter('pay_export')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class OrderPrePurchase:
    """商品确认页面"""
    params = get_parameter('prePurchase')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CreateOrder:
    """创建商品订单"""
    params = get_parameter('CreateOrder')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CreateOrder1:
    """创建商品订单"""
    params = get_parameter('CreateOrder_1')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetPayment:
    """获取支付信息"""
    params = get_parameter('getPayment')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class RepayOrder:
    """订单重新支付"""
    params = get_parameter('repay_order')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetDetailByOrderId:
    """查询订单详情"""
    params = get_parameter('getDetailByOrderId')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class GetOrders:
    """获取订单列表"""
    params = get_parameter('getOrders')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class CancelOrders:
    """取消订单"""
    params = get_parameter('cancel_Order')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])


class PayCallBack:
    """支付回调（后端使用）"""
    params = get_parameter('PayCallBack')
    case_data = []
    for i in range(0, len(params)):
        case_data.append(params[i])
