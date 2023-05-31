// Convert Range
export function convertRange(value, r1, r2, round = true) {
    let output = ((value - r1[0]) * (r2[1] - r2[0])) / (r1[1] - r1[0]) + r2[0];
    output = round == true ? Math.round(output) : output;
    return output;
}

// Responsive width
export function getMaxW(side) {
    let maxW = Math.floor(window.innerWidth / 2 - 1);

    switch (side) {
        case 'center':
            maxW = Math.floor(window.innerWidth - 1);

            if (window.innerWidth >= 720) {
                maxW = Math.floor(window.innerWidth / 3 - 1);
            }
            break;

        default:
            if (window.innerWidth >= 720) {
                maxW = Math.floor(window.innerWidth / 3 - 1);
            }
            break;
    }

    return maxW;
}
