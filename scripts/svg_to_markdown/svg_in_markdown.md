# Instructions on how to make an SVG In Markdown

I will break this down into an algorithm you must follow to the letter for it to work. Do the algorithm step by step.

## 1. Make the SVG String

The SVG should be in the following format(minus the markdown formatting i added)
```html
<svg width="250" height="250" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
  <text x="50" y="55" font-size="9" text-anchor="middle" fill="black">Hello</text>
  <more content here...>
</svg>
```

## 2. Remove all spaces
in this example you should end up with this(minus the markdown):

```html
<svg width="250" height="250" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" /><text x="50" y="55" font-size="9" text-anchor="middle" fill="black">Hello</text><more content here...></svg>
```

## 2. Convert the SVG String to base64

You must convert the SVG string to base64.
It should look like this:

```base64
PHN2ZyB3aWR0aD0yNTAgaGVpZ2h0PTI1MCB4bWxucz1odHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2Zz48Y2lyY2xlIGN4PTUwIGN5PTUwIHI9NDAgc3Ryb2tlPWdyZWVuIHN0cm9rZS13aWR0aD00IGZpbGw9eWVsbG93IC8+PHRleHQgeD01MCB5PTU1IGZvbnQtc2l6ZT05IHRleHQtYW5jaG9yPW1pZGRsZSBmaWxsPWJsYWNrPkhlbGxvPC90ZXh0Pjxtb3JlIGNvbnRlbnQgaGVyZS4uLj48L3N2Zz4K
```

## 3. Come up with a name for the image.

The name of the image should be relevant to the kind of image you are making and be descriptive. in this example the name will be "Circle with Greeting".

## 4. Putting it all together
Now you need to put the Name and the Base64 encoded SVG string into markdown, it should be in this format:
```python
f"![{image_title}](data:image/svg+xml;base64,{svg_str_base64})"
```

Our example will look like this:

```markdown
![Circle with Greeting](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0yNTAgaGVpZ2h0PTI1MCB4bWxucz1odHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2Zz48Y2lyY2xlIGN4PTUwIGN5PTUwIHI9NDAgc3Ryb2tlPWdyZWVuIHN0cm9rZS13aWR0aD00IGZpbGw9eWVsbG93IC8+PHRleHQgeD01MCB5PTU1IGZvbnQtc2l6ZT05IHRleHQtYW5jaG9yPW1pZGRsZSBmaWxsPWJsYWNrPkhlbGxvPC90ZXh0Pjxtb3JlIGNvbnRlbnQgaGVyZS4uLj48L3N2Zz4K)
```

Now paste the inclosed markdown in, so the image is rendered to the user.
