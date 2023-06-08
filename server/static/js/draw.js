let stroking = false;
let ctx;
let cv;

let pos = {
	x: -1,
	y: -1,
}

export const setCanvas = (context, canvas) => {
	ctx = context;
	cv = canvas;
};

export const moveHandler = (event) => {
	if (stroking) {
		ctx.moveTo(pos.x, pos.y);
		ctx.lineTo(event.offsetX, event.offsetY);
		ctx.stroke();
		pos.x = event.offsetX;
		pos.y = event.offsetY;
	}
};
export const downHandler = (event) => {
	pos.x = event.offsetX;
	pos.y = event.offsetY;
	ctx.beginPath();
	stroking = true;
};
export const upHandler = (event) => {
	stroking = false;
	ctx.closePath();
};

export const reset = (event) => {
	ctx.clearRect(0, 0, 256, 256);
	ctx.fillStyle = '#ffffff';
	ctx.fillRect(0, 0, 256, 256);
};
