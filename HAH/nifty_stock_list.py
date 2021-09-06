import pandas as pd

def nifty():
    df = pd.read_csv(r'C:\Users\H&H\PycharmProjects\trading\beta1\nifty.csv')
    nfty = df["NIFTY 50"].tolist()
    # print(nfty)
    return nfty

nifty()

def nifty_next_50():
    df = pd.read_csv(r'F:\trading\nifty list\NIFTY_NEXT_50.csv')
    nfty_nxt_50 = df["NIFTY_NEXT_50"].tolist()
    # print(nfty_nxt_50)
    return nfty_nxt_50

nifty_next_50()

def nifty_midcap_100():
    df = pd.read_csv(r'F:\trading\nifty list\NIFTY_MIDCAP_100.csv')
    nfty_mdcp_100 = df["NIFTY_MIDCAP_100"].tolist()
    # print(nfty_mdcp_100)
    return nfty_mdcp_100

nifty_midcap_100()

def nifty_bank():
    df = pd.read_csv(r'F:\trading\nifty list\NIFTY_BANK.csv')
    nfty_bnk = df["NIFTY_BANK"].tolist()
    # print(nfty_bnk)
    return nfty_bnk

nifty_bank()

def nifty_midcap_50():
    df = pd.read_csv(r'F:\trading\nifty list\NIFTY_MIDCAP_50.csv')
    nfty_mdcp_50 = df["NIFTY_MIDCAP_50"].tolist()
    # print(nfty_mdcp_50)
    return nfty_mdcp_50

nifty_midcap_50()

def nifty_auto():
    df = pd.read_csv(r'F:\trading\nifty list\NIFTY_AUTO.csv')
    nfty_auto = df["NIFTY_AUTO"].tolist()
    # print(nfty_auto)
    return nfty_auto

nifty_auto()

def nifty_energy():
    df = pd.read_csv(r'F:\trading\nifty list\NIFTY_AUTO.csv')
    nfty_energy = df["NIFTY_AUTO"].tolist()
    # print(nfty_energy)
    return nfty_energy

nifty_energy()

def nifty_financial_service():
    df = pd.read_csv(r'F:\trading\nifty list\NIFTY_FINANCIAL_SERVICES.csv')
    nfty_fin_srv = df["NIFTY_FINANCIAL_SERVICES"].tolist()
    # print(nfty_fin_srv)
    return nfty_fin_srv

nifty_financial_service()

def nifty_equity_to_trade():
    df = pd.read_csv(r'F:\trading\nifty list\EQUITY_TO_TRADE.csv')
    nfty_eqty_to_trd = df["EQUITY_TO_TRADE"].tolist()
    # print(nfty_eqty_to_trd)
    return nfty_eqty_to_trd

nifty_equity_to_trade()

def nifty_metal():
    df = pd.read_csv(r'F:\trading\nifty list\NIFTY_METAL.csv')
    nfty_metal = df["NIFTY_METAL"].tolist()
    # print(nfty_metal)
    return nfty_metal

nifty_metal()

def nifty_it():
    df = pd.read_csv(r'F:\trading\nifty list\NIFTY_IT.csv')
    nfty_it = df["NIFTY_IT"].tolist()
    # print(nfty_it)
    return nfty_it

nifty_it()

def nifty_healthcare():
    df = pd.read_csv(r'F:\trading\nifty list\NIFTY_HEALTHCARE.csv')
    nfty_healthcare = df["NIFTY_HEALTHCARE"].tolist()
    # print(nfty_healthcare)
    return nfty_healthcare

nifty_healthcare()

def nifty_oil_and_gas():
    df = pd.read_csv(r'F:\trading\nifty list\NIFTY_OIL_AND_GAS.csv')
    nfty_oil_and_gas = df["NIFTY_OIL_AND_GAS"].tolist()
    # print(nfty_oil_and_gas)
    return nfty_oil_and_gas

nifty_oil_and_gas()

