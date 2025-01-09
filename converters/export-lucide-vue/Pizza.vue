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
    <path d="M15 11h.01" />
    <path d="M11 15h.01" />
    <path d="M16 16h.01" />
    <path d="m2 16 20 6-6-20A20 20 0 0 0 2 16" />
    <path d="M5.71 17.11a17.04 17.04 0 0 1 11.4-11.4" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>