import { defineConfig, loadEnv } from 'vite';

import common from './vite.config.base.js';

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
    const env = loadEnv(mode, process.cwd(), '');

    return {
        ...common,
        base: env.VITE_BASE_URL,
        build: {
            sourcemap: true,
            rollupOptions: {
                // plugins: [controller_workaround()],
            },
        },
    };
});

function controller_workaround() {
    return {
        name: 'controller_workaround',
        load(id) {
            if (path.basename(id) === 'gamecontroller.js') {
                let code = fs.readFileSync(id, 'utf-8');
                code += 'exports.gameController = gameController;';
                return { code };
            } else if (path.basename(id) === 'gamecontroller.min.js') {
                let code = fs.readFileSync(id, 'utf-8');
                code += 'exports.gameController = gameController;';
                return { code };
            } else {
                return null;
            }
        },
    };
}