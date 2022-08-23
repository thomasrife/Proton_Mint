from event import Event

transfer = Event('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef')
mint = Event('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef', 
'0x0000000000000000000000000000000000000000000000000000000000000000')
aprove_for_all = Event('0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31')
sale_price_set = Event('0xe23ea816dce6d7f5c0b85cbd597e7c3b97b2453791152c0b94e5e5c5f314d2f0')
universe_set = Event('0xf28fa0fe2abe5dad2066ebce6edc9d403e4facb3603e47e6c0e7ea3e57dfe032')
test_4 = Event(
            '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef', 
            '0x000000000000000000000000ab1a1410ea40930755c1330cc0fb3367897c8c41',
            '0x0000000000000000000000002f7ebf58fd493d362357fa1bb88b3888c1cd513b',
            '0x000000000000000000000000000000000000000000000000000000000000026d'
            )

dict_of_events = {
    'Transfer': transfer, 
    'Mint': mint, 
    'AproveForAll': aprove_for_all, 
    'SalePriceSet': sale_price_set, 
    'UniverseSet': universe_set,
    'Test_4': test_4
    }
