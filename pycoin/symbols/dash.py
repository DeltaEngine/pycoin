from pycoin.networks.bitcoinish import create_bitcoinish_network
from pycoin.coins.dash.Tx import Tx as DashTx
from pycoin.coins.dash.Block import Block as DashBlock

#See https://github.com/dashevo/dashcore-lib/blob/master/lib/networks.js
network = create_bitcoinish_network(
    symbol="DASH", network_name="Dash", subnet_name="mainnet", tx=DashTx, block=DashBlock,
    wif_prefix_hex="cc", address_prefix_hex="4c", pay_to_script_prefix_hex="10",
    bip32_prv_prefix_hex="02fe52f8", bip32_pub_prefix_hex="02fe52cc",
    magic_header_hex="bf0c6bbd", default_port=9999,
    dns_bootstrap=[
        'dnsseed.darkcoin.io',
        'dnsseed.dashdot.io',
        'dnsseed.masternode.io',
        'dnsseed.dashpay.io',
    ])
