# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
import datetime

def execute(filters=None):
    columns = ["Letter","Number"]
    data = [['c',2],['a',2],['t',8],['s',7]]
    chart = {'data':{'labels':['d','o','g','s'],'datasets':[{'values':[3,6,4,7]}]},'type':'bar'}
    report_summary = [
    {"label":"cats","value":2287,'indicator':'Red'},
    {"label":"dogs","value":3647,'indicator':'Blue'}
    ]
    return columns, data,None,chart, report_summary