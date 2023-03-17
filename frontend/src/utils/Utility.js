// Convert Range
export function convertRange(value, r1, r2, round = true) {
    let output = ((value - r1[0]) * (r2[1] - r2[0])) / (r1[1] - r1[0]) + r2[0];
    output = round == true ? Math.round(output) : output;
    return output;
}
