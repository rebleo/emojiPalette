# emojiPalette

project by [aarón montoya-moraga](https://github.com/aamontoya89), [rebecca (marks) leopold](https://github.com/rebleo), [xiwei huang](https://github.com/thisisXiweiHuang).

built with on [js-emoji](https://github.com/iamcal/js-emoji)

september 2016

![](img1.png)

![](img2.png)

////////

init() 1) need to scrape this page for data set. reb is thinking Python maybe? <http://www.unicode.org/emoji/charts/full-emoji-list.html> There should be a number of classification systems so the more data we retain from this the better. idea { "Code string", ":shortcut code:", "actual emoji machine's clipboard" (is there another way of doing this?), "key words"}

This cheat sheet is helpful but not comprehensive - <http://www.webpagefx.com/tools/emoji-cheat-sheet/>

2) CREATE DATA-SET // CLASSIFICATIONS 1) COLOR - Pixel values - need to write a script that will evaluate an image and categorize it by it's RGB pixel values to read png files of emoji images & classify them by color.

```
- will need to pour all images into a folder and run a script through it that does the above
2) CATEGORIES - we can get to this later
```

3) write our own functions. do we want to build on the existing emojiJS library or pull from it & write our own?

4) need to ideate - emoji as color value/fill, emoji as image object, etc.

Things to consider: <http://www.unicode.org> <http://p5js.org/libraries/> <http://a16z.com/2016/08/02/emoji/> <https://en.wikipedia.org/wiki/Emoji>
