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
    <path d="M21 12h-8" />
    <path d="M21 6H8" />
    <path d="M21 18h-8" />
    <path d="M3 6v4c0 1.1.9 2 2 2h3" />
    <path d="M3 10v6c0 1.1.9 2 2 2h3" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>