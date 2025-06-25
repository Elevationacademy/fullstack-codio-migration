Similar to functions, we can modify classes to accept Generics, and by that, allowing them to function based on the given type.

In the example below, we can see how we define a class which could receive a Generic type. In this example we just hold the generic type, allowing the class to hold various types.
```js
class ImageType<DataType> {
	data: DataType;
	height: number;
	width: number;

	constructor(data: DataType, height: number, width: number) {
		this.data = data;
		this.height = height;
		this.width = width
	};
}
const imageType = new ImageType<string>("John", 480, 640);
```
Once we accept a Generic type, we could then add a ‘switch’ or an ‘if-then-else’ block to distinguish between the types and perform type-specific operations like in the example below.
```ts
function toPNG(data: DataType): DataType {
	// Check if the data is of class ‘Buffer’
	if (Buffer.isBuffer(data)) {
		…
	// Check if the data is of class ‘Array’
	} else if (Array.isArray(data)) {
		…
	// Check if the data is of type ‘string’
	} else if (typeof data === 'string') {
		…	
	// Otherwise, throw an exception
	} else {
		throw 'toPNG only accepts arrays, buffers, or strings'
	}
}
```
