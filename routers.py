from app import api

from resourses.articles_resource import ArticlesResource
api.add_resource(ArticlesResource, '/articles', '/articles/<int:article_id>')

from resourses.catalogs_resource import CatalogsResource
api.add_resource(CatalogsResource, '/catalogs', '/catalogs/<int:catalog_id>')

from resourses.customers_resource import CustomersResource
api.add_resource(CustomersResource, '/customers',
                 '/customers/<int:customer_id>')

from resourses.goods_resource import GoodsResource
api.add_resource(GoodsResource, '/goods', '/goods/<int:good_id>')

from resourses.goodsizes_resource import GoodsizesResource
api.add_resource(GoodsizesResource, '/goodsizes',
                 '/goodsizes/<int:goodsize_id>')

from resourses.goodcolors_resource import GoodcolorsResource
api.add_resource(GoodcolorsResource, '/goodcolors',
                 '/goodcolors/<int:goodcolor_id>')

from resourses.addresses_resource import AddressesResource
api.add_resource(AddressesResource, '/addresses',
                 '/addresses/<int:address_id>')

from resourses.goodorders_resource import GoodordersResource
api.add_resource(GoodordersResource, '/goodorders',
                 '/goodorders/<int:goodorder_id>')

from resourses.orderitems_resource import OrderitemsResource
api.add_resource(OrderitemsResource, '/orderitems',
                 '/orderitems/<int:orderitem_id>')
