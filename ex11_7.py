start_ch = 0x05  # 시작 문자
addr = 2  # 주소
seqNo = 1  # 순서 번호
msg = input('your message: ')

frame = {"start": start_ch, "address": addr, "seq_no": seqNo, "length": len, "payload": msg}

capsule = f'''{frame['start']:c}{frame['address']:02d}{frame['seq_no']:04d}{frame['length']({frame['payload']}):04d}{frame['payload']}'''
print(capsule)
