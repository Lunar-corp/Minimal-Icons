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
    <path d="M14 4c0-1.1.9-2 2-2" />
    <path d="M20 2c1.1 0 2 .9 2 2" />
    <path d="M22 8c0 1.1-.9 2-2 2" />
    <path d="M16 10c-1.1 0-2-.9-2-2" />
    <path d="m3 7 3 3 3-3" />
    <path d="M6 10V5c0-1.7 1.3-3 3-3h1" />
    <rect width="8" height="8" x="2" y="14" rx="2" />
    <path d="M14 14c1.1 0 2 .9 2 2v4c0 1.1-.9 2-2 2" />
    <path d="M20 14c1.1 0 2 .9 2 2v4c0 1.1-.9 2-2 2" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>