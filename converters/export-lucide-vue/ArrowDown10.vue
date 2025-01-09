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
    <path d="m3 16 4 4 4-4" />
    <path d="M7 20V4" />
    <path d="M17 10V4h-2" />
    <path d="M15 10h4" />
    <rect x="15" y="14" width="4" height="6" ry="2" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>