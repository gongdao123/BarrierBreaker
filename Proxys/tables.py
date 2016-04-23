from models import HttpProxy
from table import Table
from table.columns import Column, DatetimeColumn

class HttpProxyTable(Table):
    id = Column(field='id', header=u'#')
    name = Column(field='nick_name', header=u'Nick Name' )
    hash_id = Column(field='hash_id', header=u'Hash ID' )
    lan_ip = Column(field='lan_ip', header=u'Proxy Address')
    modified_datetime = DatetimeColumn(field='modified_datetime', format='%Y-%m-%d %H:%M:%S', header=u'Update Time')
    status = Column(field='status', header=u'Status')
    class Meta:
        model = HttpProxy
