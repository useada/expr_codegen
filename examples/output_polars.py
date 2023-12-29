# this code is auto generated by the expr_codegen
# https://github.com/wukan1986/expr_codegen
# 此段代码由 expr_codegen 自动生成，欢迎提交 issue 或 pull request

import re

import numpy as np
import polars as pl
import polars.selectors as cs

from loguru import logger

# from polars_ta.prefix.ta import *  # noqa
# from polars_ta.prefix.talib import *  # noqa
# from polars_ta.prefix.tdx import *  # noqa
from polars_ta.prefix.wq import *  # noqa

# TODO: 数据加载或外部传入
df = df_input


def func_0_ts__asset__date(df: pl.DataFrame) -> pl.DataFrame:
    df = df.sort(by=["date"])
    # ========================================
    df = df.with_columns(
        # _x_0 = ts_mean(OPEN, 10)
        _x_0=(ts_mean(pl.col("OPEN"), 10)),
        # expr_6 = ts_delta(OPEN, 10)
        expr_6=(ts_delta(pl.col("OPEN"), 10)),
        # expr_7 = ts_rank(OPEN + 1, 10)
        expr_7=(ts_rank(pl.col("OPEN") + 1, 10)),
        # _x_1 = ts_mean(CLOSE, 10)
        _x_1=(ts_mean(pl.col("CLOSE"), 10)),
        # expr_5 = -ts_corr(OPEN, CLOSE, 10)
        expr_5=(-ts_corr(pl.col("OPEN"), pl.col("CLOSE"), 10)),
    )
    return df


def func_0_cs__date(df: pl.DataFrame) -> pl.DataFrame:
    # ========================================
    df = df.with_columns(
        # _x_7 = cs_rank(OPEN)
        _x_7=(cs_rank(pl.col("OPEN"))),
    )
    return df


def func_0_gp__date__sw_l1(df: pl.DataFrame) -> pl.DataFrame:
    # ========================================
    df = df.with_columns(
        # _x_5 = gp_demean(sw_l1, CLOSE)
        _x_5=(neutralize_demean(pl.col("CLOSE"))),
        # _x_6 = gp_rank(sw_l1, CLOSE)
        _x_6=(cs_rank(pl.col("CLOSE"))),
    )
    return df


def func_1_cs__date(df: pl.DataFrame) -> pl.DataFrame:
    # ========================================
    df = df.with_columns(
        # _x_2 = cs_rank(_x_0)
        _x_2=(cs_rank(pl.col("_x_0"))),
        # _x_3 = cs_rank(_x_1)
        _x_3=(cs_rank(pl.col("_x_1"))),
    )
    return df


def func_1_ts__asset__date(df: pl.DataFrame) -> pl.DataFrame:
    df = df.sort(by=["date"])
    # ========================================
    df = df.with_columns(
        # _x_8 = ts_mean(_x_7, 10)
        _x_8=(ts_mean(pl.col("_x_7"), 10)),
        # expr_8 = ts_rank(expr_7 + 1, 10)
        expr_8=(ts_rank(pl.col("expr_7") + 1, 10)),
    )
    return df


def func_2_cl(df: pl.DataFrame) -> pl.DataFrame:
    # ========================================
    df = df.with_columns(
        # expr_2 = _x_2 + _x_5 + _x_6 - Abs(log(_x_1))
        expr_2=(pl.col("_x_2") + pl.col("_x_5") + pl.col("_x_6") - abs_(log(pl.col("_x_1")))),
    )
    return df


def func_2_ts__asset__date(df: pl.DataFrame) -> pl.DataFrame:
    df = df.sort(by=["date"])
    # ========================================
    df = df.with_columns(
        # expr_3 = ts_mean(_x_2, 10)
        expr_3=(ts_mean(pl.col("_x_2"), 10)),
        # expr_1 = -ts_corr(_x_2, _x_3, 10)
        expr_1=(-ts_corr(pl.col("_x_2"), pl.col("_x_3"), 10)),
    )
    return df


def func_2_cs__date(df: pl.DataFrame) -> pl.DataFrame:
    # ========================================
    df = df.with_columns(
        # expr_4 = cs_rank(_x_8)
        expr_4=(cs_rank(pl.col("_x_8"))),
    )
    return df


# logger.info("start...")


df = df.sort(by=["date", "asset"])
df = df.group_by(by=["asset"], maintain_order=False).map_groups(func_0_ts__asset__date)
df = df.group_by(by=["date"], maintain_order=False).map_groups(func_0_cs__date)
df = df.group_by(by=["date", "sw_l1"], maintain_order=False).map_groups(func_0_gp__date__sw_l1)
df = df.group_by(by=["date"], maintain_order=False).map_groups(func_1_cs__date)
df = df.group_by(by=["asset"], maintain_order=False).map_groups(func_1_ts__asset__date)
df = func_2_cl(df)
df = df.group_by(by=["asset"], maintain_order=False).map_groups(func_2_ts__asset__date)
df = df.group_by(by=["date"], maintain_order=False).map_groups(func_2_cs__date)


# #========================================func_0_ts__asset__date
# _x_0 = ts_mean(OPEN, 10)
# expr_6 = ts_delta(OPEN, 10)
# expr_7 = ts_rank(OPEN + 1, 10)
# _x_1 = ts_mean(CLOSE, 10)
# expr_5 = -ts_corr(OPEN, CLOSE, 10)
# #========================================func_0_cs__date
# _x_7 = cs_rank(OPEN)
# #========================================func_0_gp__date__sw_l1
# _x_5 = gp_demean(sw_l1, CLOSE)
# _x_6 = gp_rank(sw_l1, CLOSE)
# #========================================func_1_cs__date
# _x_2 = cs_rank(_x_0)
# _x_3 = cs_rank(_x_1)
# #========================================func_1_ts__asset__date
# _x_8 = ts_mean(_x_7, 10)
# expr_8 = ts_rank(expr_7 + 1, 10)
# #========================================func_2_cl
# expr_2 = _x_2 + _x_5 + _x_6 - Abs(log(_x_1))
# #========================================func_2_ts__asset__date
# expr_3 = ts_mean(_x_2, 10)
# expr_1 = -ts_corr(_x_2, _x_3, 10)
# #========================================func_2_cs__date
# expr_4 = cs_rank(_x_8)

"""
[OPEN, CLOSE, sw_l1, expr_7]
"""

"""
expr_1 = -ts_corr(cs_rank(ts_mean(OPEN, 10)), cs_rank(ts_mean(CLOSE, 10)), 10)
expr_2 = cs_rank(ts_mean(OPEN, 10)) + gp_demean(sw_l1, CLOSE) + gp_rank(sw_l1, CLOSE) - Abs(log(ts_mean(CLOSE, 10)))
expr_3 = ts_mean(cs_rank(ts_mean(OPEN, 10)), 10)
expr_4 = cs_rank(ts_mean(cs_rank(OPEN), 10))
expr_5 = -ts_corr(OPEN, CLOSE, 10)
expr_6 = ts_delta(OPEN, 10)
expr_8 = ts_rank(expr_7 + 1, 10)
expr_7 = ts_rank(OPEN + 1, 10)
"""

# drop intermediate columns
df = df.drop(columns=list(filter(lambda x: re.search(r"^_x_\d+", x), df.columns)))

# shrink
df = df.select(cs.all().shrink_dtype())
df = df.shrink_to_fit()

# logger.info('done')

# save
# df.write_parquet('output.parquet', compression='zstd')

# print(df.tail(5))

# 向外部传出数据
df_output = df
