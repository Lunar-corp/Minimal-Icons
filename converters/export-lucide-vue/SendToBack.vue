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
    <rect x="14" y="14" width="8" height="8" rx="2" />
    <rect x="2" y="2" width="8" height="8" rx="2" />
    <path d="M7 14v1a2 2 0 0 0 2 2h1" />
    <path d="M14 7h1a2 2 0 0 1 2 2v1" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>