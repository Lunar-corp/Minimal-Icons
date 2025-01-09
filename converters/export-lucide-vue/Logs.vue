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
    <path d="M13 12h8" />
    <path d="M13 18h8" />
    <path d="M13 6h8" />
    <path d="M3 12h1" />
    <path d="M3 18h1" />
    <path d="M3 6h1" />
    <path d="M8 12h1" />
    <path d="M8 18h1" />
    <path d="M8 6h1" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>