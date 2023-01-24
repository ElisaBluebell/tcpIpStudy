# 소켓 정보 찾기
import socket


def get_constants(prefix):
    """
    소켓 모듈의 속성 문자와 맵핑되는 속성값을 딕셔너리로 반환한다.
    """
    return {
        getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)
    }


# 'AF_', 'SOCK_', 'IPPROTO_'로 시작하는 소켓 속성 문자를 속성값과 맵핑시키는 딕셔너리를 만든다.
families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.dongyang.ac.kr', 'http'):

    # 5-튜플 응답을 unpacking한다.
    family, socktype, proto, canonname, sockaddr = response

    print('Family           :', families[family])
    print('Type             :', types[socktype])
    print('Protocol         :', protocols[proto])
    print('Canonical name   :', canonname)
    print('Socket address   :', sockaddr)
    print()

