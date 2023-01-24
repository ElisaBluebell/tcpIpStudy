import socket


def get_constants(prefix):
    '''딕셔너리의 경우 키와 값을 이런 식으로 정의할 수도 있는듯, 리스트를 포함한 다른 자료형의 경우는
    에러가 출력됨, 속성값:속성 문자 상수를 매칭한 딕셔너리를 통해 속성 문자 상수를 출력하기 위해 반환
    '''
    return {getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)}


# 각각 해당 속성값에 해당하는 상수명으로 시작하는 문자에 대응하는 딕셔너리 생성함
families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# 기본적으로 http의 포트 번호는 80번이라기에 이곳저곳에 'http' 대신 80을 넣어보는데 정상적으로 실행되지 않음. 왜지
for response in socket.getaddrinfo('www.naver.co.kr', 'http'):

    family, socktype, proto, canonname, sockaddr = response

    print('Family           :', families[family])
    print('Type             :', types[socktype])
    print('Protocol         :', protocols[proto])
    print('Canonical name   :', canonname)
    print('Socket address   :', sockaddr)
    print()
