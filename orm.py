# Product.objects.all()
# # SELECT * FROM products;
#
# Product.objects.get(id=1)
# SELECT * FROM products WHERE id = 1;

# Product.objects.filter(условие1, условие2)
# SELECT * FROM products WHERE условие1, AND условие2;

# Product.objects.filter(Q(условие1)|Q(условие2))
# SELECT * FROM products WHERE условие1 OR условие2;
#
# Product.objects.filter(~Q(условие))
# Product.objects.exclude(условие)
# SELECT * FROM products WHERE NOT условие;

# Product.objects.filter(price__gt=50000)  #больше
# SELECT * FROM products WHERE price > 50000;

# Product.objects.filter(price__lt=50000)  #меньше
# SELECT * FROM products WHERE price < 50000;

# Product.objects.filter(price=50000)  #равно
# SELECT * FROM products WHERE price = 50000;

# Product.objects.filter(~Q(price=50000))
# SELECT * FROM products WHERE NOT price = 50000;

# Product.objects.filter(price__gte=50000)
# SELECT * FROM products WHERE price >= 50000;

# Product.objects.filter(price__lte=50000)
# SELECT * FROM products WHERE price <= 50000;

# Product.objects.filter(category_id__in=['phones', 'notebooks'])
# SELECT * FROM product WHERE category_id IN ('phones', 'notebooks');

# Product.objects.filter(price__range=[20000, 50000])
# SELECT * FROM products WHERE price BETWEEN 20000 AND 50000;

# Product.objects.filter(name__exact='Iphone')
# SELECT * FROM products WHERE name LIKE 'Iphone';
# Product.objects.filter(name__iexact='Iphone')
# SELECT * FROM products WHERE name ILIKE 'Iphone';

# Product.objects.filter(name__startwith='Iphone')
# SELECT * FROM products WHERE name LIKE 'Iphone%';
# Product.objects.filter(name__istartwith='Iphone')
# SELECT * FROM products WHERE name ILIKE 'Iphone%';

# Product.objects.filter(name__contains='Iphones')
# SELECT * FROM products WHERE name LIKE '%Iphone%';
# Product.objects.filter(name__icontains='Iphones')
# SELECT * FROM products WHERE name ILIKE '%Iphone%';

# Product.objects.filter(name__endswith='Iphones')
# SELECT * FROM products WHERE name LIKE '%Iphone';
# Product.objects.filter(name__iendswith='Iphones')
# SELECT * FROM products WHERE name ILIKE '%Iphone';

# Product.objects.order_by('price')
# SELECT * FROM products ORDER BY price ASC;

# Product.objects.order_by('-price')
# SELECT * FROM products ORDER BY price DESC;

# Product.objects.only('name')
# SELECT name FROM products;

# Product.objects.only('name', 'price')  #запрашивает указанные поля из table
# SELECT name, 'price' FROM products;

# Product.objects.defer('name', 'price')  # исключает указанные поля из table
# SELECT id, description, category_id FROM products;

# Product.objects.count()
# SELECT COUNT(*) FROM products;

# Product.objects.filter(...).count()
# SELECT COUNT(*) FROM products WHERE ...;

# Product.objects.create(name='Apple Iphone12', description='hdbhfvrbe', price=78000, category_id='phones')
# INSERT INTO products (name, description, price, category_id) VALUES \ ('Apple Iphone12', 'hrbfer', 78000, 'phones')

# Product.objects.bulk_create([
#     Product(....),
#     Product(....)
# ]) #множественное создание

# Product.objects.update(price=50000)
# UPDATE products SET price=50000;
#
# Product.objects.filter(...).update(price=50000)
# UPDATE products SET price=50000 WHERE ...;
#
# Product.objects.filter(id=1).update(price=50000)
# UPDATE products SET price=50000 WHERE id=1;
#
# product = Product.objects.get(id=1)
# product.price = 50000
# product.save()

# Product.objects.delete()
# DELETE FROM products;

# Product.objects.filter(category_id='phones').delete()
# DELETE FROM products WHERE category_id = 'phones';

# Product.objects.filter(id=1).delete()
# DELETE FROM products WHERE id=1;

# product = Product.objects.get(id=1)
# product.delete()
