root = $("#mw-content-text > div > div:nth-child(22)")
graphics = root.children("div")
graphics.each(function(i, e) {
    let img = $(e).find("img").attr("src")
    let text = $(e).children().last().text()
    console.log(`img: ${img}, text: ${text}`)
})

data = graphics.map(function(i, e) {
    let img = $(e).find("img").attr("src")
    let text = $(e).children().last().text()
    return {img, text}
}).get()
