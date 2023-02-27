import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { viteStaticCopy } from 'vite-plugin-static-copy'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    /*
    viteStaticCopy({
      targets: [
        {
          src: './dist/assets/**.*',
          dest: '../../backend/assets'
        },
        {
          src: './dist/index.html',
          dest: '../../backend/templates'
        },
      ]
    })
    */
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
