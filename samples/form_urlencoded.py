import asyncio

from okie import Okie, FormURLEncodedBuilder, HttpRequestType


async def main():
    okie = Okie(timeout=60)

    # builders use different intermediate buffers
    with FormURLEncodedBuilder() as builder:
        builder.add_field("key", "value")
        builder.add_field("key1", "value1")

    response = await okie.request(
        HttpRequestType.GET,
        url="http://httpbin.org/anything",
        data_builder=builder,
    )

    print(response.body.decode())

    # let's reuse builder
    builder.clean()
    with builder:
        builder.add_field("hm", "think")
        builder.add_field("greeting", "bonjour!")
        builder.add_field("name", "value")

    response = await okie.request(
        "GET",
        url="http://httpbin.org/anything",
        data_builder=builder,
    )

    print(response.body.decode())
    print({**response.headers})


asyncio.run(main())
