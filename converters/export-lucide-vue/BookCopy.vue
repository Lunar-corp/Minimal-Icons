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
    <path d="M2 16V4a2 2 0 0 1 2-2h11" />
    <path d="M5 14H4a2 2 0 1 0 0 4h1" />
    <path d="M22 18H11a2 2 0 1 0 0 4h11V6H11a2 2 0 0 0-2 2v12" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>