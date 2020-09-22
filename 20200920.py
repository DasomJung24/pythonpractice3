total_count = len(products)
results = []

for data in products:
    price              = int(data.price)
    discount_rate      = int(data.discount_rate)
    discount_price     = 0

    if discount_rate != 0:
        discount_price = price // 100 * (100 - discount_rate)

    add = {
        'main_image'    : data.main_image,
        'name'          : data.name,
        'total_count'   : total_count,
        'price'         : price,
        'discount_rate' : discount_rate,
        'discount_price': discount_price,
        'product_id'    : data.id
    }

    results.append(add)



# 위 식을 리스트 컴프리헨션으로 변경!!!

results = [{
    'main_image': data.main_image,
    'name': data.name,
    'total_count': len(products),
    'price': int(data.price),
    'discount_rate' : int(data.discount_rate),
    'discount_price': int(data.price) // 100 * (100 - int(data.discount_rate)) if int(data.discount_rate) != 0 else 0,
    'product_id' : data.id} for data in products]