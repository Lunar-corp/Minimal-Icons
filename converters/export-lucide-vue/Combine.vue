<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <rect width="8" height="8" x="2" y="2" rx="2" />
    <path d="M14 2c1.1 0 2 .9 2 2v4c0 1.1-.9 2-2 2" />
    <path d="M20 2c1.1 0 2 .9 2 2v4c0 1.1-.9 2-2 2" />
    <path d="M10 18H5c-1.7 0-3-1.3-3-3v-1" />
    <polyline points="7 21 10 18 7 15" />
    <rect width="8" height="8" x="14" y="14" rx="2" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>