命令行
******

quantlib提供一些在命令行使用的快捷命令，通过 ``python -m quant`` 来调用这些命令。

数据集管理
##########

quantlib使用 ``quant.common.localizer.Localizer`` 来缓存数据，这些数据默认保存在 ``~/.quantlib/data`` 目录下，每个数据集保存成一个hdf5文件。
每个文件中可以有多个DataFrame数据。 ``python -m quant data`` 命令可以用来管理这些数据集。

列出数据集名称
==============

..  code-block::
    bash
    
    python -m quant data ls

列出当前缓存的所有数据集名称

删除某个数据集
==============

有时，缓存的数据可能已经过时，我们需要重新计算一些结果，这就需要把已有的数据集删除。可以使用

..  code-block::
    bash

    python -m quant data rm "数据集名"

来删除指定的数据集。

数据表管理
##########

quantlib的WindDB会把从wind数据库取得的原始数据缓存在wind_table.h5中。久而久之这个数据集会非常庞大。如果每次更新数据都要把整个数据集删除的话非常不方便。
因此，quantlib提供了额外的命令行 ``python -m quant table`` 来专门管理wind_table中的数据表。

列出所有的键
============

..  code-block::
    bash

    python -m quant table ls

增量更新所有的表
================

..  code-block::
    bash

    python -m quant table update

增量更新指定的表
================

..  code-block::
    bash

    python -m quant table update "表名"

删除某个数据表
==============

..  code-block::
    bash

    python -m quant table rm "表名"

删除某个表的字段
================

..  code-block::
    bash
    
    python -m quant table rm "表名/字段名"

策略回测
########

..  code-block::
    bash

    python -m quant backtest 文件名.h5 键名 --freq 换仓周期

quantlib会调用ConstraintStrategy来对指定的数据进行回测。


