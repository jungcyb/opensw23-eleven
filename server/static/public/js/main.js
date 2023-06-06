$(document).ready(() => {
	const canvas = document.getElementById("mycanvas");
	const ctx = canvas.getContext("2d");

	setCanvas(ctx, canvas);

	$("#convert-draw").on("click", captureHandler)

	$("#reset").on("click", reset);

	$(canvas).on("mousemove", moveHandler);
	$(canvas).on("mousedown", downHandler);
	$(canvas).on("mouseup", upHandler);
});