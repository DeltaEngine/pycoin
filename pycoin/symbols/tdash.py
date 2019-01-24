from pycoin.networks.bitcoinish import create_bitcoinish_network
from pycoin.coins.dash.Tx import Tx as DashTx
from pycoin.coins.dash.Block import Block as DashBlock

#See https://github.com/dashevo/dashcore-lib/blob/master/lib/networks.js
network = create_bitcoinish_network(
    symbol="tDASH", network_name="Dash", subnet_name="testnet", tx=DashTx, block=DashBlock,
    wif_prefix_hex="ef", address_prefix_hex="8c", pay_to_script_prefix_hex="13",
    bip32_prv_prefix_hex="3a8061a0", bip32_pub_prefix_hex="3a805837",
    magic_header_hex="cee2caff", default_port=19999,
    dns_bootstrap=[
        'testnet-seed.darkcoin.io',
        'testnet-seed.dashdot.io',
        'test.dnsseed.masternode.io',
    ])
